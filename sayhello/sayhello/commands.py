import click
from sayhello import app,db
from sayhello.models import Comment

@app.cli.command()
@click.option("--count",default=20,help="Quantity of messages, default is 20.")
def forge(count):
    from faker import Faker

    db.drop_all()
    db.create_all()
    fake = Faker()
    click.echo("Working...")

    for i in range(count):
        comment = Comment(
            name = fake.name(),
            comment = fake.sentence(),
            time = fake.date_time_this_year()

        )

        db.session.add(comment)
        db.session.commit()
        click.echo("Created %d fake comments" %count)