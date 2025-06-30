Email Subscription System
A Django-based email subscription system with asynchronous email processing using Celery. Users can subscribe by entering their name and email, and the system automatically sends confirmation emails in the background.
Key Features:

Contact model for storing subscriber information (name & email)
Automated email sending via Gmail SMTP
Asynchronous task processing with Celery and Redis
Admin panel for managing contacts
Simple web form for subscription
How it works:
When users submit the contact form, their data is saved to the database and a confirmation email is sent asynchronously using Celery tasks, ensuring smooth user experience without blocking the main thread.
Perfect for newsletters, blog subscriptions, or any service requiring email notifications!
