
class TaskPriority():
    """Task Priority Options"""
    LOW = 'lo'
    MEDIUM = 'me'
    HIGH = 'hi'
    CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

class TaskStatus():
    """Task Status Options"""
    OPEN = 'op'
    DONE = 'do'
    CHOICES = (
        (OPEN, 'Open'),
        (DONE, 'Done'),
    )


# Utility functions
def to_external(enum, internal_value):
    """From internal database value to external"""
    match = filter(lambda x: x[0] == internal_value, enum.CHOICES)
    if len(match) > 0:
        return match[0][1]
    else:
        raise Exception('Invalid choice value')

def to_internal(enum, external_value):
    """From external to internal database value"""
    match = filter(lambda x: x[1] == external_value, enum.CHOICES)
    if len(match) > 0:
        return match[0][0]
    else:
        raise Exception('Invalid choice value')
