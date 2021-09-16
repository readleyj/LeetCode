defmodule Solution do
  @spec can_construct(ransom_note :: String.t(), magazine :: String.t()) :: boolean
  def can_construct(ransom_note, magazine) do
    magazine_char_freqs = Enum.frequencies(String.graphemes(magazine))
    ransom_char_freqs = Enum.frequencies(String.graphemes(ransom_note))

    Enum.reduce_while(ransom_char_freqs, true, fn {char, freq}, _ ->
      if freq > Map.get(magazine_char_freqs, char, 0), do: {:halt, false}, else: {:cont, true}
    end)
  end
end
