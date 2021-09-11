defmodule Solution do
  def gcd(a, 0), do: a
  def gcd(a, b), do: gcd(b, rem(a, b))

  @spec find_gcd(nums :: [integer]) :: integer
  def find_gcd(nums) do
    gcd(Enum.max(nums), Enum.min(nums))
  end
end
