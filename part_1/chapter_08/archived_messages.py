copy_messages = ["msg1", "msg2", "msg2"]
sent_messages = []


def show_messages(copy_messages):
    for msg in copy_messages:
        print(f">>> {msg}")
        sent_messages.append(msg)


show_messages(copy_messages)
print(sent_messages)
print(copy_messages)
