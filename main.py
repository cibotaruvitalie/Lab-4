from abc import ABC, abstractmethod

# Chain of Responsibility pattern
class MessageHandler(ABC):
    def __init__(self, next_handler=None):
        self._next_handler = next_handler
    
    def handle(self, message):
        if not self._next_handler:
            return False
        return self._next_handler.handle(message)
    
    @abstractmethod
    def can_handle(self, message):
        pass


class TextHandler(MessageHandler):
    def can_handle(self, message):
        return isinstance(message, str)
    
    def handle(self, message):
        if self.can_handle(message):
            print(f"Received text message: {message}")
            return True
        else:
            return super().handle(message)
        

class ImageHandler(MessageHandler):
    def can_handle(self, message):
        return isinstance(message, bytes)
    
    def handle(self, message):
        if self.can_handle(message):
            print("Received image message")
            # Process image message
            return True
        else:
            return super().handle(message)


# Command pattern
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class SendMessageCommand(Command):
    def __init__(self, message, mediator):
        self._message = message
        self._mediator = mediator
    
    def execute(self):
        self._mediator.send_message(self._message)


# Mediator pattern
class Mediator:
    def __init__(self):
        self._handlers = []
    
    def add_handler(self, handler):
        self._handlers.append(handler)
    
    def send_message(self, message):
        for handler in self._handlers:
            if handler.can_handle(message):
                handler.handle(message)
                break


# Observer pattern
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class User(Observer):
    def __init__(self, name, mediator):
        self._name = name
        self._mediator = mediator
    
    def send_message(self, message):
        command = SendMessageCommand(message, self._mediator)
        command.execute()
    
    def update(self, message):
        print(f"{self._name} received message: {message}")


# Usage example
if __name__ == "__main__":
    mediator = Mediator()
    text_handler = TextHandler()
    image_handler = ImageHandler()
    mediator.add_handler(text_handler)
    mediator.add_handler(image_handler)
    
    user1 = User("Alice", mediator)
    user2 = User("Bob", mediator)
    
    mediator.add_handler(user1)
    mediator.add_handler(user2)
    
    user1.send_message("Hello Bob!")
    user2.send_message(b"\x89PNG...")
