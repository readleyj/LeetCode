defmodule Solution do
  @key_idx_mapper %{"type" => 0, "color" => 1, "name" => 2}

  @spec count_matches(items :: [[String.t()]], rule_key :: String.t(), rule_value :: String.t()) ::
          integer
  def count_matches(items, rule_key, rule_value) do
    Enum.count(items, fn item ->
      Enum.at(item, @key_idx_mapper[rule_key]) == rule_value
    end)
  end
end

# Slightly fancier solution

# defmodule Solution do
#   @spec count_matches(items :: [[String.t()]], rule_key :: String.t(), rule_value :: String.t()) ::
#           integer
#   def count_matches(items, rule_key, rule_value) do
#     Enum.count(items, fn item ->
#       case {item, rule_key} do
#         {[^rule_value, _, _], "type"} -> true
#         {[_, ^rule_value, _], "color"} -> true
#         {[_, _, ^rule_value], "name"} -> true
#         _ -> false
#       end
#     end)
#   end
# end
