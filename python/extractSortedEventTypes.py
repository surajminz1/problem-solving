from collections import defaultdict

def get_sorted_user_events(events):
    """
    Groups events by user_id and returns a dict mapping user_id
    to a chronologically sorted list of their event_types.
    """
    user_event_data = defaultdict(list)

    # Group events by user_id, storing timestamp for sorting
    for event in events:
        user_id = event['user_id']
        print(user_id)
    result = {}

    # Sort events for each user and extract event_types

    return result

# Example usage with the provided data:
events = [
    {'user_id': 101, 'event_type': 'click', 'timestamp': 1678886400},
    {'user_id': 102, 'event_type': 'view', 'timestamp': 1678886450},
    {'user_id': 101, 'event_type': 'purchase', 'timestamp': 1678886500},
    {'user_id': 103, 'event_type': 'view', 'timestamp': 1678886550},
    {'user_id': 101, 'event_type': 'view', 'timestamp': 1678886600},
    {'user_id': 102, 'event_type': 'click', 'timestamp': 1678886650},
]

print(get_sorted_user_events(events))
# Expected Output:
# {
#  101: ['click', 'purchase', 'view'],
#  102: ['view', 'click'],
#  103: ['view']
# }