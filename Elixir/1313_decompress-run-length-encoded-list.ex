defmodule Solution do
  @spec decompress_rl_elist(nums :: [integer]) :: [integer]
  def decompress_rl_elist(nums) do
    Enum.chunk_every(nums, 2) |> Enum.flat_map(fn [freq, val] -> List.duplicate(val, freq) end)
  end
end
