# **Messaging System**

This is a simple messaging system implemented in Python, which uses several design patterns to achieve its functionality. The patterns used are:

- Chain of Responsibility
- Command
- Mediator
- Observer

**Requirements**

- Python 3.x

**How to use**

1. Clone this repository to your local machine.
2. Navigate to the messaging\_system directory.
3. Run python main.py to start the program.

When the program starts, it creates a Mediator object and adds two User objects to it (Alice and Bob). The Mediator object also adds two message handlers to its chain of responsibility: TextHandler and ImageHandler.

You can simulate sending messages by calling the send\_message method of a User object. For example, to send a text message from Alice to Bob, you can run:

python

alice.send\_message("Hello Bob!")

To send an image message from Bob to Alice, you can run:

python

bob.send\_message(b"\x89PNG...")

**Design Patterns Used**

**Chain of Responsibility**

The Chain of Responsibility pattern is used to handle incoming messages. The MessageHandler abstract base class defines the interface for message handlers, and its subclasses (TextHandler and ImageHandler) implement specific handling logic. The Mediator class uses a chain of message handlers to handle incoming messages. When a new message arrives, the Mediator iterates over the chain of handlers until it finds one that can handle the message.

**Command**

The Command pattern is used to encapsulate the act of sending a message into an object (SendMessageCommand). The User class uses a command to send messages to the Mediator.

**Mediator**

The Mediator pattern is used to decouple the User objects from each other and from the message handling logic. The Mediator class acts as a central hub that receives messages and dispatches them to the appropriate handlers. When a new message arrives, the Mediator sends a notification to all registered observers (User objects), which then update themselves accordingly.

**Observer**

The Observer pattern is used to notify the User objects when a new message arrives. The User class acts as an observer that receives notifications when a new message arrives. When a new message arrives, the Mediator sends a notification to all registered observers (User objects), which then update themselves accordingly.

**Conclusion**

This program demonstrates the power of using design patterns to solve real-world problems. By using a combination of Chain of Responsibility, Command, Mediator, and Observer patterns, we were able to implement a simple messaging system that is flexible, extensible, and easy to maintain.