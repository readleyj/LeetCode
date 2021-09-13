defmodule Solution do
  @spec is_anagram(s :: String.t(), t :: String.t()) :: boolean
  def is_anagram(s, t) do
    Enum.frequencies(to_charlist(s)) == Enum.frequencies(to_charlist(t))
  end
end
