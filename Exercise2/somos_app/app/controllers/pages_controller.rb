class PagesController < ApplicationController
  def home
  end
  def somos
  end

  def tech
  end

  def math
    if params[:a].present? && params[:b].present? && params[:c].present?
      a = params[:a].to_f
      b = params[:b].to_f
      c = params[:c].to_f

      discriminant = b**2 - 4 * a * c

      @quadratic_result =
        if discriminant < 0
          "No real roots"
        elsif discriminant == 0
          x = -b / (2 * a)
          "One real root: x = #{x.round(3)}"
        else
          x1 = (-b + Math.sqrt(discriminant)) / (2 * a)
          x2 = (-b - Math.sqrt(discriminant)) / (2 * a)
          "Two real roots: x₁ = #{x1.round(3)}, x₂ = #{x2.round(3)}"
        end
    end

    if params[:n].present?
      n = params[:n].to_i
      if n < 0
        @factorial_result = "Factorial is not defined for negative numbers"
      else
        @factorial_result = (1..n).inject(1, :*).to_s
      end
    end
  end
end
