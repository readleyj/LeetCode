defmodule Solution do
  @spec build_array(nums :: [integer]) :: [integer]
  def build_array(nums) do
    Enum.map(nums, &Enum.at(nums, &1))
  end
end
