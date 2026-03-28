import re
from pathlib import Path
import sys

def extract_toctree_from_index(index_path: str) -> list[tuple[str, list[str]]]:
    """
    Extracts (caption, [entries]) tuples from index.md toctree. This is used
    later to generate AI-readable TOC-tree for llms.txt.
    """
    content = Path(index_path).read_text()
    
    # Find all toctree blocks
    toctree_pattern = re.compile(
        r'```\{toctree\}.*?```',
        re.DOTALL
    )
    
    sections: list[tuple[str, list[str]]] = []
    for block in toctree_pattern.finditer(content):
        block_text = block.group()
        
        # Extract caption
        caption_match = re.search(r':caption:\s*(\S.*?)\s*$', block_text, re.MULTILINE)
        if not caption_match:
            continue
        caption = caption_match.group(1).strip()
        
        # Extract entries (paths between caption and closing ```)
        entries: list[str] = []
        in_toctree = False
        for line in block_text.split('\n'):
            if line.strip().startswith('```'):
                if in_toctree:
                    break
                in_toctree = True
                continue
            if in_toctree and line.strip() and not line.strip().startswith(':') and not line.strip().startswith('```'):
                entries.append(line.strip())
        
        if caption and entries:
            sections.append((caption, entries))
    
    return sections


def generate_toc_markdown(sections: list[tuple[str, list[str]]]) -> str:
    """
    Generates TOC markdown based on 'selections' gneerated from
    'extract_toctree_from_index'.
    """
    lines = [
        "# Table of Contents",
        ""
    ]
    
    for caption, entries in sections:
        lines.append(f"## {caption}")
        for entry in entries:
            # Remove file extension if present
            entry = re.sub(r'\.(md|rst)$', '', entry)
            # Add trailing slash for URL format
            if not entry.endswith('/'):
                entry = entry + '/'
            lines.append(f"- {entry}")
        lines.append("")
    
    return '\n'.join(lines)


def update_llms_txt(index_path: Path, template_path: Path, output_path: Path) -> None:
    """
    Generates the TOC and merge it with a template file into an output file.
    The template file should contain the marker "@replace-table-of-content"
    to indicate where the TOC should be injected.
    """
    # Extract new TOC
    sections = extract_toctree_from_index(str(index_path))
    new_toc = generate_toc_markdown(sections)
    
    # Remove the "# Table of Contents" header that generate_toc_markdown adds
    # We want to inject only the content, not the header,
    # as the template might provide its own header structure.
    lines = new_toc.splitlines()
    if lines and lines[0].startswith("# Table of Contents"):
        new_toc = "\n".join(lines[1:]).strip()

    # Read template llms.txt
    template_content = template_path.read_text()

    # Define marker
    marker = "@replace-table-of-content"
    
    # Merge content
    if marker not in template_content:
        # If no marker, just append to the end
        new_content = template_content.rstrip() + "\n\n" + new_toc
    else:
        # Split at the marker and replace it with the new TOC
        before, after = template_content.split(marker, 1)
        new_content = before.rstrip() + "\n\n" + new_toc + "\n" + after.lstrip()

    # Clean up empty lines
    new_content = re.sub(r'\n\s*\n', '\n\n', new_content)
    
    output_path.write_text(new_content)
    print(f"Generated {output_path} with new TOC injected at '{marker}'.")

if __name__ == '__main__':
    script_dir = Path(__file__).parent
    
    # We use llms_template.txt as the source
    template_file = script_dir / 'llms_template.txt'
    
    # If the template doesn't exist, we can't sync safely
    if not template_file.exists():
        print(f"Error: Template file {template_file} not found.")
        sys.exit(1)
        
    update_llms_txt(script_dir / 'index.md', template_file, script_dir / 'llms.txt')
