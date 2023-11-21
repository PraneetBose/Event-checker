import json
import os

EVENTS_FILE = 'events.json'

def load_events():
    if os.path.exists(EVENTS_FILE):
        with open(EVENTS_FILE, 'r') as file:
            events = json.load(file)
        return events
    else:
        return []

def save_events(events):
    with open(EVENTS_FILE, 'w') as file:
        json.dump(events, file, indent=2)

def display_events(events):
    for event in events:
        print(f"Event ID: {event['id']}")
        print(f"Title: {event['title']}")
        print(f"Description: {event['description']}")
        print(f"Date: {event['date']}")
        print("----------------------------")

def create_event(events, title, description, date):
    event_id = len(events) + 1
    new_event = {'id': event_id, 'title': title, 'description': description, 'date': date}
    events.append(new_event)
    save_events(events)
    print("Event created successfully.")

def edit_event(events, event_id, title, description, date):
    for event in events:
        if event['id'] == event_id:
            event['title'] = title
            event['description'] = description
            event['date'] = date
            save_events(events)
            print("Event edited successfully.")
            return
    print("Event not found.")

def delete_event(events, event_id):
    events = [event for event in events if event['id'] != event_id]
    save_events(events)
    print("Event deleted successfully.")

def main():
    print("Event Management System")

    events = load_events()

    while True:
        print("\n1. Display Events")
        print("2. Create Event")
        print("3. Edit Event")
        print("4. Delete Event")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_events(events)
        elif choice == '2':
            title = input("Enter the title: ")
            description = input("Enter the description: ")
            date = input("Enter the date: ")
            create_event(events, title, description, date)
        elif choice == '3':
            event_id = int(input("Enter the event ID to edit: "))
            title = input("Enter the new title: ")
            description = input("Enter the new description: ")
            date = input("Enter the new date: ")
            edit_event(events, event_id, title, description, date)
        elif choice == '4':
            event_id = int(input("Enter the event ID to delete: "))
            delete_event(events, event_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
