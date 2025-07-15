from document import PDFDocument, WordDocument, TextDocument, Document

class DocumentFactory:
    @staticmethod
    def create_document(doc_type: str) -> Document:
        doc_type = doc_type.lower()
        if doc_type == "pdf":
            return PDFDocument()
        elif doc_type == "word":
            return WordDocument()
        elif doc_type == "text":
            return TextDocument()
        else:
            raise ValueError("Unknown document type")
