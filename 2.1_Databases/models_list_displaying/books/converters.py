from datetime import date


class DateConverter:
   regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
   format = '%Y-%m-%d'

   def to_python(self, value: str) -> date:
       return date.fromisoformat(value)

   def to_url(self, value: date) -> str:
       return value.strftime(self.format)
