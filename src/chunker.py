def chunk_text(text,chunk_size = 500 , overlap = 100):
    paragraphs = text.split("\n\n")
    chunks = [] 
    start = 0
    for paragraph in paragraphs:
        paragraph = paragraph.strip()

        if not paragraph:
            continue

        if len(paragraph)<=chunk_size:
            chunks.append(paragraph)

        else:
            start = 0
            while start<len(paragraph):
                end = start+chunk_size
                chunk = paragraph[start:end]
                chunks.append(chunk)
                start+=chunk_size-overlap
    
    return chunks