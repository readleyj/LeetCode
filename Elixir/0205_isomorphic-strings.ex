defmodule Solution do
  @spec is_isomorphic(s :: String.t(), t :: String.t()) :: boolean
  def is_isomorphic(s, t) do
    encode_str(s) == encode_str(t)
  end

  def encode_str(s) do
    {encoded_chars, _} =
      Enum.map_reduce(String.graphemes(s), %{}, fn char, char_mapper ->
        cur_letter_idx = map_size(char_mapper)

        cond do
          Map.has_key?(char_mapper, char) -> {char_mapper[char], char_mapper}
          true -> {cur_letter_idx + 1, Map.put(char_mapper, char, cur_letter_idx + 1)}
        end
      end)

    Enum.join(encoded_chars)
  end
end
