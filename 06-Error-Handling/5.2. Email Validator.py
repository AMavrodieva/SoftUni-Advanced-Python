class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


command = input()
valid_domain = {'com', 'bg', 'org', 'net'}
while True:
    if command == "End":
        break
    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")
    name, domain_name = command.split("@")
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    domain = domain_name.split(".")[1]
    if domain not in valid_domain:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(valid_domain)}")

    print('Email is valid')
    command = input()
