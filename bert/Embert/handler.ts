import type { StartTaskMessage, TaskContext, HandlerResult } from '@blocks-network/sdk';

async function postData(data) {
  const url = 'http://127.0.0.1:8000/';

  try {
    const response = await fetch(url, {
      method: 'POST',
      body: data,
    });

    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const json = await response.json();
    console.log('Success:', json);
    return json;
  } catch (error) {
    console.error('Error:', error.message);
    return error;
  }
}



/**
 * Handler function for the agent.
 * Receives a task and echoes back the input text.
 */
export default async function handler(
  task: StartTaskMessage,
  ctx?: TaskContext,
): Promise<HandlerResult> {
  const text = task.requestParts?.[0]?.text ?? '';
  ctx?.reportStatus('Processing...');
  const resp = await postData(text);
  console.log('=================');
  console.log(resp);
  console.log('=================');

  // Replace this with your agent logic
  return {
    artifacts: [{ data: JSON.stringify(resp), mimeType: 'text/plain' }],
  };
}
