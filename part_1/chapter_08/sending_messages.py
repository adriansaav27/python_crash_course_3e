sent_messages = []


def show_messages(messages):
    for msg in messages:
        print(f">>> {msg}")
        sent_messages.append(msg)


show_messages(["msg1", "msg2", "msg2"])
print(sent_messages)
