from dataclasses import dataclass

@dataclass
class Transaction:
     user_id: int
     location: int
     amount: float
     transaction_type: str
     transaction_id = None
     date: int

@dataclass
class Purchase:
      transaction_id = None
      category: str
      store: str
      name: str
      figure: float
      amount: int
      date: int
      purchase_id = None
