room_1_students = int(input())
room_2_students = int(input())
room_3_students = int(input())
room_1_desks = room_1_students // 2 + room_1_students % 2
room_2_desks = room_2_students // 2 + room_2_students % 2
room_3_desks = room_3_students // 2 + room_3_students % 2
total_desks = room_1_desks + room_2_desks + room_3_desks
print(total_desks)