from __future__ import annotations

from car_searcher.notifications.notifiers.abc.notifier import CarAd, Notifier

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class EmailNotifier(Notifier):
    def __init__(
        self,
        smtp_server: str,
        smtp_port: int,
        sender_email: str,
        sender_password: str,
        recipient_email: str,
    ):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email

    def notify(self, ads: list[CarAd]) -> None:
        """Send email with new ads."""
        if not ads:
            return

        msg = MIMEMultipart()
        msg["Subject"] = f"Znaleziono {len(ads)} nowych ogłoszeń!"
        msg["From"] = self.sender_email
        msg["To"] = self.recipient_email

        html_content = f"""
        <html>
        <body>
            <h2>Znaleziono {len(ads)} nowych ogłoszeń!</h2>
            <table border="1">
                <tr>
                    <th>Tytuł</th>
                    <th>Cena</th>
                    <th>Lokalizacja</th>
                    <th>Link</th>
                </tr>
        """

        for ad in ads:
            html_content += f"""
                <tr>
                    <td>{ad.title}</td>
                    <td>{ad.price} zł</td>
                    <td>{ad.location}</td>
                    <td><a href="{ad.url}">Link do ogłoszenia</a></td>
                </tr>
            """

        html_content += """
                </table>
            </body>
        </html>
        """

        msg.attach(MIMEText(html_content, "html"))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
        except Exception as e:  # TODO: more specific exception
            print(f"Error during e-mail send: {e}")  # TODO: add logger after implementation
