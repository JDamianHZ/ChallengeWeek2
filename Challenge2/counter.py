class DocumentCounter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DocumentCounter, cls).__new__(cls)
            cls._instance.count = 0
        return cls._instance

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
