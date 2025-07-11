def build_prompt(ticket_text, queue_list):
    return f"""You are a support triage assistant. Classify the following ticket into one of the queues listed.

-----
Ticket information:
{ticket_text}
-----

Possible queues: {", ".join(queue_list)}

What is the most appropriate queue for this ticket? Just output the name of the queue."""
