def build_prompt(ticket_text, queue_list):
    return f"""You are a support triage assistant. Classify the following ticket into one of the queues listed.

-----
Ticket information:
{ticket_text}
-----

Possible queues: {", ".join(queue_list)}

What is the most appropriate queue for this ticket? Just output the name of the queue."""


def build_prompt_fewShot(ticket_text, queue_list, fewshot_text):
    return f"""You are a support triage assistant. Classify the following IT ticket into one of the queues listed.

-----
Ticket information:
{ticket_text}
-----

Possible queues: {", ".join(queue_list)}

Queue Details:
Technical Support: Technical issues and support requests.
Customer Service: Customer inquiries and service requests.
Billing and Payments: Billing issues and payment processing.
Product Support: Support for product-related issues.
IT Support: Internal IT support and infrastructure issues.
Returns and Exchanges: Product returns and exchanges.
Sales and Pre-Sales: Sales inquiries and pre-sales questions.
Human Resources: Employee inquiries and HR-related issues.
Service Outages and Maintenance: Service interruptions and maintenance.
General Inquiry: General inquiries and information requests.

-----
Here are some examples:
{fewshot_text}
-----

What is the most appropriate queue for this ticket? Just output the name of the queue."""
