from typing import Optional

class Payable:
  """A protocol class for objects that can be paid for."""

  PayType = {"CASH", "CARD", "PHONE"}

  def get_pay_type(self) -> "PayType":
    if self._pay_type not in self.PayType:
      raise ValueError(f"Invalid payment method: {self._pay_type}")
    else:
       return self._pay_type

  def set_pay_type(self, payment_method: "PayType") -> None:
    if payment_method not in self.PayType:
      raise ValueError(f"Invalid payment method: {payment_method}")
    self._pay_type = payment_method
