from agents.data_agent import data_agent
from langchain_core.messages import HumanMessage

if __name__ == "__main__":
    
    
    #Below 2 invoke messages should call ETL Extract and transform tool and result to be pushed to respective folder
    # response = data_agent.invoke(
    #     {"messages":[HumanMessage(content=f"""I want to extract the data from the API endpoint 'https://pokeapi.co/api/v2/pokemon' and save it to data/extract folder in the csv folder""")],
    #      "route_response": ""}
    # )
    
    # response = data_agent.invoke(
    #     {"messages":[HumanMessage(content=f"""I want to transform the data stored in the 'C:/Projects/DATA_AGENT/data/extract/extracted_data.csv' file 
    #         and save the transformed data in the 'C:/Projects/DATA_AGENT/data/transform' folder in the csv format.
    #         The transformation should filter the data to show bulbasaur pokemon only.""")],
    #      "route_response": ""}
    # )
    
    #Below invoke messages should call SQL Agent
    response = data_agent.invoke(
        {"messages":[HumanMessage(content=f"""What are all the different types of vehicle colours we have in vehicles table""")],
         "route_response": ""}
    )
    
    # response = data_agent.invoke(
    #     {"messages":[HumanMessage(content=f"""What are the different types of Payment Methods we have in our database""")],
    #      "route_response": ""}
    # )

    print(response)