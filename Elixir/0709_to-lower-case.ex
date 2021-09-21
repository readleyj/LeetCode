defmodule Solution do
  @spec to_lower_case(s :: String.t()) :: String.t()
  def to_lower_case(s) do
    for <<char <- s>>, into: "" do
      cond do
        char in ?A..?Z -> <<char + 32>>
        true -> <<char>>
      end
    end
  end
end
