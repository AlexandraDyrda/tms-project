class TaskValidator:
    def is_title_valid(self, title: str) -> bool:
        if not title:
            return False
        return bool(title.strip())
