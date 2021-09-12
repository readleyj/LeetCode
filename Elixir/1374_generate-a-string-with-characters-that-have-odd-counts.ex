defmodule Solution do
  @spec generate_the_string(n :: integer) :: String.t()
  def generate_the_string(n) do
    String.duplicate("a", n - 1) <>
      case(rem(n, 2)) do
        1 -> "a"
        0 -> "b"
      end
  end
end
