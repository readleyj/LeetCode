defmodule Solution do
  @spec check_record(s :: String.t()) :: boolean
  def check_record(s) do
    !!Enum.reduce_while(String.graphemes(s), {0, 0}, fn char, acc ->
      {num_consecutive_late, num_absent} = acc

      acc =
        cond do
          char == "L" -> {num_consecutive_late + 1, num_absent}
          char == "A" -> {0, num_absent + 1}
          true -> {0, num_absent}
        end

      case acc do
        {_, num_absent} when num_absent >= 2 ->
          {:halt, false}

        {num_consecutive_late, _} when num_consecutive_late >= 3 ->
          {:halt, false}

        {num_consecutive_late, num_absent} ->
          {:cont, {num_consecutive_late, num_absent}}
      end
    end)
  end
end
