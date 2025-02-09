from fastapi import Body


class CustomerPayload:

    def __init__(
        self,
        name: str = Body(description="Customer name"),
        mod_no: str = Body(description="customer mobile number"),
        remaining_amount:float  = Body(description="Remaining amount"),
    ):

        self.name = name
        self.mod_no = mod_no
        self.remaining_amount = remaining_amount
