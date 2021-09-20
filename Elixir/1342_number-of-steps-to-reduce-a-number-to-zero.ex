defmodule Solution do
  @spec number_of_steps(num :: integer) :: integer
  def number_of_steps(num) do
    Stream.unfold(num, fn num ->
      cond do
        num == 0 -> nil
        rem(num, 2) == 0 -> {num, div(num, 2)}
        rem(num, 2) == 1 -> {num, num - 1}
      end
    end)
    |> Enum.to_list()
    |> length()
  end
end
