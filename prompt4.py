class Kitten:
    def __init__(self, front_leg_length, rear_leg_length, num_eyes, has_tail, is_furry):
        self.front_leg_length = front_leg_length
        self.rear_leg_length = rear_leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe_kitten(self):
        tail_status = "Has a tail" if self.has_tail else "Does not have a tail"
        furry_status = "Has fur" if self.is_furry else "Does not have fur"
        
        description = (
            f"Kitten Parameters:"
            f"- Arm Length: {self.front_leg_length}"
            f"- Leg Length: {self.rear_leg_length}"
            f"- Number of Eyes: {self.num_eyes}"
            f"- {tail_status}"
            f"- {furry_status}"
        )
        print(description)

def main():
    my_kitten = Kitten(front_leg_length=7, rear_leg_length=8.5, num_eyes=2, has_tail=True, is_furry=True)
    my_kitten.describe_kitten()

if __name__ == "__main__":
    main()
