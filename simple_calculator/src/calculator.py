class Calculator:
    def __init__(self):
        self.reset()

    def reset(self):
        self.current_value = 0
        self.previous_value = None
        self.pending_operation = None
        self.new_number = True
        self.error_state = False
        self.negative_first = False

    def handle_number(self, number: str) -> str:
        if self.error_state:
            self.reset()

        # Prevent numbers from becoming too large
        current_str = str(self.current_value) if not self.new_number else ""
        if len(current_str + number) > 10:  # Limit to 10 digits
            return self._format_number(self.current_value)

        if self.new_number:
            self.current_value = int(number)
            self.new_number = False
        else:
            self.current_value = int(current_str + number)

        if self.negative_first:
            self.current_value = -self.current_value
            self.negative_first = False

        return self._format_number(self.current_value)

    def handle_operation(self, operation: str) -> str:
        if self.error_state:
            self.reset()

        if operation == '-':
            if self.new_number:
                self.negative_first = True
                return "-"

        if self.pending_operation:
            try:
                self.current_value = self._calculate()
            except Exception as e:
                self.error_state = True
                return "Error"

        self.previous_value = self.current_value
        self.pending_operation = operation
        self.new_number = True
        return self._format_number(self.current_value)

    def calculate_result(self) -> str:
        if self.error_state:
            self.reset()
            return "0"
        
        if not self.pending_operation:
            return self._format_number(self.current_value)

        # If we have a pending operation but new_number is still True,
        # it means no second number was entered
        if self.new_number:
            return self._format_number(self.current_value)

        try:
            result = self._calculate()
            self.current_value = result
            self.pending_operation = None
            self.new_number = True
            return self._format_number(result)
        except ZeroDivisionError:
            self.error_state = True
            return "Error: Division by zero"
        except Exception as e:
            self.error_state = True
            return "Error"

    def _calculate(self) -> float:
        if self.pending_operation == '+':
            return self.previous_value + self.current_value
        elif self.pending_operation == '-':
            return self.previous_value - self.current_value
        elif self.pending_operation == '*':
            return self.previous_value * self.current_value
        elif self.pending_operation == '/':
            if self.current_value == 0:
                raise ZeroDivisionError
            return self.previous_value / self.current_value
        return self.current_value

    def _format_number(self, number: float) -> str:
        str_num = str(number)
        if '.' in str_num:
            str_num = str_num.rstrip('0').rstrip('.')
        return str_num
