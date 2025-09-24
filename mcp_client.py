import asyncio
import logging
import sys

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("mcp-client")

async def connect_to_mcp():
    from mcp.client.streamable_http import streamablehttp_client
    from mcp import ClientSession

    headers = {
        "Authorization": "Bearer <auth_token>",
        "Mcp-Session-Id": "session-" + str(asyncio.current_task().get_name())
    }
    
    server_url = "https://ah-api.merge.dev/api/v1/tool-packs/<tool_pack_id>/registered-users/<registered_user_id>/mcp"
    
    logger.info(f"Connecting to MCP server: {server_url}")
    
    try:
        async with streamablehttp_client(server_url, headers=headers) as (read_stream, write_stream, _):
            logger.info("Connection established, creating ClientSession")
            async with ClientSession(read_stream, write_stream) as session:
                logger.info("Initializing session with protocol version 2024-11-05")
                await session.initialize()
                
                logger.info("Listing tools")
                tools_result = await session.list_tools()
                logger.info("\nMCP Tools:")
                logger.info(tools_result)

                # Example call
                # tool_name = "<tool_name>"
                # try:
                #     tool_result = await session.call_tool(tool_name, {"<tool-args>": {}})
                #     logger.info(f"\nResults from {tool_name}: {tool_result}")
                # except Exception as e:
                #     logger.error(f"Error calling tool {tool_name}: {e}")
    except Exception as e:
        logger.exception(f"Error in MCP client: {e}")

async def main():
    logger.info("Starting MCP client")
    await connect_to_mcp()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Program terminated by user")
        sys.exit(0)
    except Exception as e:
        logger.exception(f"Unhandled exception: {e}")
        sys.exit(1)
