defmodule Solution do
  @spec fizz_buzz(n :: integer) :: [String.t()]
  def fizz_buzz(n) do
    1..n
    |> Enum.map(fn num ->
      case {rem(num, 3), rem(num, 5), num} do
        {0, 0, _} -> "FizzBuzz"
        {0, _, _} -> "Fizz"
        {_, 0, _} -> "Buzz"
        {_, _, num} -> Integer.to_string(num)
      end
    end)
  end
end
