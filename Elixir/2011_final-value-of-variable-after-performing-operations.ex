defmodule Solution do
  @spec final_value_after_operations(operations :: [String.t()]) :: integer
  def final_value_after_operations(operations) do
    Enum.reduce(
      operations,
      0,
      &(&2 +
          case &1 do
            "++X" -> 1
            "X++" -> 1
            "--X" -> -1
            "X--" -> -1
          end)
    )
  end
end
