def to_camel_case(s):
    parts = s.split('_')
    return parts[0] + ''.join(p.title() for p in parts[1:])
