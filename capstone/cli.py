import time
import click
import schedule

try:
    from .api_client import fetch_crypto_data
    from .pdf_generator import generate_pdf_report
except ImportError:
    from api_client import fetch_crypto_data
    from pdf_generator import generate_pdf_report

def run_pipeline(output):
    click.echo("Fetching latest market data...")
    data = fetch_crypto_data()
    click.echo(f"Generating PDF report: {output}...")
    generate_pdf_report(data, output)
    click.echo("Report successfully generated!")


@click.group()
def cli():
    """Enterprise Automation CLI Tool"""
    pass


@cli.command()
@click.option(
    "--output",
    default="crypto_report.pdf",
    help="Output file name for the PDF report.",
)
def generate(output):
    """Generate a one-time PDF report."""
    run_pipeline(output)


@cli.command()
@click.option(
    "--interval", default=60, help="Scheduling interval in seconds."
)
@click.option(
    "--output", default="scheduled_report.pdf", help="Output file name."
)
def start_scheduler(interval, output):
    """Run automated recurring report generation."""
    click.echo(
        f"Scheduler started. Generating report every {interval} seconds..."
    )
    schedule.every(interval).seconds.do(run_pipeline, output=output)

    # Initial run
    run_pipeline(output)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    cli()