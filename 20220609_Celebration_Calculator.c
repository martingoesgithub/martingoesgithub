int main(void)
{
    const str CELEBRATIONGRADE = "Manager"
    str grade = get_str("What's your grade?\n")

    if (grade == CELEBRATIONGRADE)
    {
        printf("Achtarmig einen reinorgeln, Herr %s!", grade)
    }
    else
    {
        printf("Nächstes Jahr klappt es bestimmt!")
    }
}
