import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama


load_dotenv()


def main():
    print("Hello from langchain-course!")

    information = """
    Elon Reeve Musk was born on June 28, 1971, in Pretoria, South Africa's administrative capital.[1][2] He is of British and Pennsylvania Dutch ancestry.[3][4] His mother, Maye (née Haldeman), is a model and dietitian born in Saskatchewan, Canada, and raised in South Africa.[5][6][7] Musk therefore holds both South African and Canadian citizenship from birth.[8] His father, Errol Musk, is a South African electromechanical engineer, pilot, sailor, consultant, emerald dealer, and property developer, who partly owned a rental lodge at Timbavati Private Nature Reserve.[9][10][11][12]
    His maternal grandfather, Joshua N. Haldeman, who died in a plane crash when Elon was a toddler, was an American-born Canadian chiropractor, aviator and political activist in the Technocracy movement[13][14] who moved to South Africa in 1950.[15] Haldeman's anti-government, anti-democratic and conspiracist views, which included the promotion of far-right antisemitic conspiracy theories,[16][17] "fanatical" support of apartheid,[17] and according to Errol Musk, support of Nazism,[15] have been suggested as an influence on Elon.[18][19][20][21] During his childhood, Elon was told stories by his grandmother of Haldeman's travels and exploits, and Elon has suggested that all of Haldeman's descendants have his "desire for adventure, exploration – doing crazy things".[22]
    """

    summmary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them."""

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summmary_template)

    llm = ChatOpenAI(temperature=0, model="gpt-5")
    #llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response)


if __name__ == "__main__":
    main()
