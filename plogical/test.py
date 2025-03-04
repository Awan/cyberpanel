# #
# # import imaplib
# # import getpass
# # from email import message_from_string
# # import socket
# #
# # import dns.resolver as dnspython
# #
# # def get_mx_records(domain):
# #     try:
# #         # Query MX records for the domain
# #         mx_records = dns.resolver.resolve(domain, 'MX')
# #         # Extract and return the MX record data
# #         return [(mx.exchange.to_text(), mx.preference) for mx in mx_records]
# #     except dns.resolver.NoAnswer:
# #         print(f"No MX records found for {domain}")
# #         return []
# #     except dns.resolver.NXDOMAIN:
# #         print(f"Domain {domain} not found")
# #         return []
# #     except Exception as e:
# #         print(f"Error: {str(e)}")
# #         return []
# #
# #
# # # IMAP server settings
# # imap_server = ''
# # imap_port = 993
# #
# # # User credentials
# # email_address = ''
# # password = ''
# #
# # # Connect to the IMAP server
# # mail = imaplib.IMAP4_SSL(imap_server, imap_port)
# #
# # # Log in to the mailbox
# # mail.login(email_address, password)
# #
# # # Select the INBOX
# # mail.select("inbox")
# #
# # # Search for all emails in the INBOX
# # result, data = mail.search(None, "ALL")
# # email_ids = data[0].split()
# #
# # # Fetch and print header information for each email
# # for email_id in email_ids:
# #     result, message_data = mail.fetch(email_id, "(BODY[HEADER.FIELDS (FROM TO SUBJECT DATE)])")
# #     raw_email = message_data[0][1].decode('utf-8')
# #     msg = message_from_string(raw_email)
# #     FromDomain = msg['From'].split('@')[1].rstrip('>')
# #     MailServer = get_mx_records(FromDomain)
# #     print(f'From Domain {FromDomain}')
# #     print(f'MX Records of the domains {MailServer}')
# #     print(f'Mail Server From Domain {MailServer}')
# #     print(f"Email ID: {email_id}")
# #     print(f"From: {msg['From']}")
# #     print(f"To: {msg['To']}")
# #     print(f"Subject: {msg['Subject']}")
# #     print(f"Date: {msg['Date']}")
# #     print("-" * 30)
# #     print(message_data)
# #
# # # Logout
# # mail.logout()
# # #
# # # # from cryptography import x509
# # # # from cryptography.hazmat.backends import default_backend
# # # #
# # # # def get_domains_covered(cert_path):
# # # #     with open(cert_path, 'rb') as cert_file:
# # # #         cert_data = cert_file.read()
# # # #         cert = x509.load_pem_x509_certificate(cert_data, default_backend())
# # # #
# # # #         # Check for the Subject Alternative Name (SAN) extension
# # # #         san_extension = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName)
# # # #
# # # #         if san_extension:
# # # #             # Extract and print the domains from SAN
# # # #             san_domains = san_extension.value.get_values_for_type(x509.DNSName)
# # # #             return san_domains
# # # #         else:
# # # #             # If SAN is not present, return the Common Name as a fallback
# # # #             return [cert.subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)[0].value]
# # # #
# # # # # Example usage
# # # # cert_path = '/etc/letsencrypt/live/cyberplanner.io/fullchain.pem'
# # # # domains_covered = get_domains_covered(cert_path)
# # # #
# # # # print("Domains covered by the certificate:")
# # # # for domain in domains_covered:
# # # #     print(domain)
#
# import dns.resolver
#
#
# def query_sbl(ip):
#     try:
#         # Construct the reverse DNS lookup domain
#         reversed_ip = '.'.join(reversed(ip.split('.')))
#         sbl_domain = reversed_ip + '.zen.spamhaus.org'
#
#         # Query the SBL DNS server
#         result = dns.resolver.resolve(sbl_domain, 'A')
#
#         # If the query returns a result, it means the IP is listed in SBL
#         return True
#     except dns.resolver.NXDOMAIN:
#         # If the domain does not exist, the IP is not listed in SBL
#         return False
#     except dns.resolver.Timeout:
#         # Handle DNS query timeout
#         print("DNS query timed out")
#         return None
#     except dns.resolver.NoAnswer:
#         # Handle no DNS answer
#         print("No DNS answer")
#
#         return None
#
#
# # Example usage
# ip_to_check = '209.85.166.5'
# result = query_sbl(ip_to_check)
# if result is True:
#     print(f"The IP {ip_to_check} is listed in Spamhaus Block List (SBL)")
# elif result is False:
#     print(f"The IP {ip_to_check} is not listed in Spamhaus Block List (SBL)")
# else:
#     print("Unable to determine SBL status for the given IP")
#
