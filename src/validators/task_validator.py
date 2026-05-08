class TaskValidator:
    def is_title_valid(self, title) -> bool:
        if title is None: return False
        return bool(title.strip())