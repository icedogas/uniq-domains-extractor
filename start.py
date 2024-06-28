# Read URLs from the input text file by specifying the encoding
with open('urls.txt', 'r', encoding='utf-8') as file:
    urls = file.readlines()

# Extract domains up to the third level from URLs
up_to_third_level_domains = []
for url in urls:
    if 'http' in url:
        # Split the domain into parts
        domain_parts = url.split('/')[2].split('.')
        if len(domain_parts) > 1:  # Check if there are at least two parts
            if domain_parts[0].lower() == 'www':
                domain_parts = domain_parts[1:]  # Remove 'www' if present
            if len(domain_parts) <= 3:  # Keep up to the third level
                up_to_third_level_domain = '.'.join(
                    domain_parts[-3:])  # Keep up to the third level
                up_to_third_level_domains.append(up_to_third_level_domain)

# Retain unique domains up to the third level
unique_up_to_third_level_domains = list(set(up_to_third_level_domains))

# Write unique domains up to the third level to a new text file
with open('new.txt', 'w') as file:
    for domain in unique_up_to_third_level_domains:
        file.write(domain + '\n')
