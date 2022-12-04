assignments = []
with open("input.txt") as f:
    for line in f:
        sections = line.strip().split(",")
        sections = (
            [int(s) for s in sections[0].split("-")],
            [int(s) for s in sections[1].split("-")],
        )
        assignments.append(sections)


def order_assignments(assignment):
    assignment0 = (
        assignment[0] if assignment[0][0] > assignment[1][0] else assignment[1]
    )
    assignment1 = (
        assignment[0] if assignment[0][0] < assignment[1][0] else assignment[1]
    )

    return assignment0, assignment1


def assignments_edges_are_equal(assignment):
    return assignment[0][0] == assignment[1][0] or assignment[0][1] == assignment[1][1]


duplicated_assignments = 0
for assignment in assignments:
    if assignments_edges_are_equal(assignment):
        duplicated_assignments += 1
    else:
        assignment0, assignment1 = order_assignments(assignment)
        if assignment0[1] < assignment1[1]:
            duplicated_assignments += 1
print(duplicated_assignments)

overlapping_assignments = 0
for assignment in assignments:
    if assignments_edges_are_equal(assignment):
        overlapping_assignments += 1
    else:
        assignment0, assignment1 = order_assignments(assignment)
        if assignment0[0] <= assignment1[1]:
            overlapping_assignments += 1
print(overlapping_assignments)
