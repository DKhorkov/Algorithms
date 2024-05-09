"""
Динамическое программирование в основном используется в задачах оптимизации. Как правило, задача для оптимизации может
иметь множество возможных решений, каждое из которых необходимо сопоставить с оставшимися для выбора оптимального.

Суть динамического программирования - это разбить задачу на подзадачи. Сначала находится оптимальное решение каждой
из подзадач, а затем выбирается оптимальное решение для поставленной задачи на основе оптимальных решений подзадач.

По сути, асимптоматическая скорость работы алгоритмов, основанных на динамическом программировании, рассчитывается как
произведение количества подзадач на количество выборов в каждой подзадаче.

Также такие задачи обычным перебором будут иметь экспоненциальную асимптоматическую скорость выполнения, например,
O(2 ^ n). Динамическое программирование позволяет сделать их полиномиальными, например, O(n ^ 2),
что асимптоматически существенно лучше. Данное улучшение производится за счет запоминание результатов решенных ранее
подзадач и обращения к ним вместо повторного вычисления.
"""