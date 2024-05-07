import os
import azure.functions as func
import logging
import psycopg2

app = func.FunctionApp()
con = psycopg2.connect(os.getenv("DATABASE_URL"))


@app.event_hub_message_trigger(
    arg_name="azeventhub",
    event_hub_name="iothub-ehub-techin510-59467401-6d881a7ae1",
    connection="IOHUB_CONNECTION_STRING",
)
def eventhub_trigger1(azeventhub: func.EventHubEvent):
    logging.info(
        "Python EventHub trigger processed an event: %s",
        azeventhub.get_body().decode("utf-8"),
    )
    with con:
        with con.cursor() as cur:
            cur.execute("SELECT * FROM books LIMIT 10")
            rows = cur.fetchall()
            logging.info("The number of books: %s", len(rows))
            cur.execute(
                "INSERT INTO messages (message) VALUES (%s)",
                (azeventhub.get_body().decode("utf-8"),),
            )
