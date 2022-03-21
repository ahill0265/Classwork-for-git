import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.layout.*;
import javafx.stage.Stage;

public class CoffeeShop extends Application {

	//UI Elements
	public Coffee order;
	public Button startButton, deleteButton, finishButton, extraShotButton, vanillaButton, creamButton, sugarButton, whippedCreamButton;
	public TextArea messageBox;
	public VBox orderButtonsBox, logBox, buttonsBox;
	public HBox optionButtonsBox;
	public BorderPane borderPane;

	//variables
	public int extraShotCount, vanillaCount, creamCount, sugarCount, whippedCreamCount;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		launch(args);
	}

	//feel free to remove the starter code from this method
	@Override
	public void start(Stage primaryStage) throws Exception {
		// TODO Auto-generated method stub
		primaryStage.setTitle("Who want's coffee!!!");
		primaryStage.setResizable(false); //hard coded dimensional design necessitates this

		borderPane = new BorderPane();
		Scene scene = new Scene(borderPane,800,600);

		//initializing and setting buttons
		startButton = new Button("Start Order");
		startButton.setStyle("-fx-base: #ffdead;");
		startButton.setOnAction(e -> startPressed());

		deleteButton = new Button("Delete Order");
		deleteButton.setStyle("-fx-base: #ffdead;");
		deleteButton.setOnAction(e -> deletePressed());

		finishButton = new Button("Finish Order");
		finishButton.setStyle("-fx-base: #ffdead;");
		finishButton.setOnAction(e -> finishPressed());

		extraShotButton = new Button("Extra Shot: +$1.20");
		extraShotButton.setStyle("-fx-base: #ffdead;");
		extraShotButton.setOnAction(e -> extraShotPressed());

		vanillaButton = new Button("Vanilla: +$1.50");
		vanillaButton.setStyle("-fx-base: #ffdead;");
		vanillaButton.setOnAction(e -> vanillaPressed());

		creamButton = new Button("Cream: +$0.50");
		creamButton.setStyle("-fx-base: #ffdead;");
		creamButton.setOnAction(e -> creamPressed());

		sugarButton = new Button("Sugar: +$0.50");
		sugarButton.setStyle("-fx-base: #ffdead;");
		sugarButton.setOnAction(e -> sugarPressed());

		whippedCreamButton = new Button("Whipped Cream: +$0.50");
		whippedCreamButton.setStyle("-fx-base: #ffdead;");
		whippedCreamButton.setOnAction(e -> whippedCreamPressed());

		//box to display messages in response to user action
		messageBox = new TextArea();
		messageBox.setMinSize(300,600);
		messageBox.setMaxSize(300, 600);
		messageBox.setEditable(false);
		messageBox.setMouseTransparent(true);
		messageBox.setFocusTraversable(false);
		messageBox.setStyle("-fx-control-inner-background: #ffdead; -fx-opacity: 0.5; -fx-font-weight: bold;");

		//organizing everything on the screen
		orderButtonsBox = new VBox(10, extraShotButton, vanillaButton, creamButton, sugarButton, whippedCreamButton);
		orderButtonsBox.setAlignment(Pos.CENTER);
		optionButtonsBox = new HBox( 10, startButton, deleteButton, finishButton);
		optionButtonsBox.setAlignment(Pos.CENTER);
		buttonsBox = new VBox(50, optionButtonsBox, orderButtonsBox);
		buttonsBox.setAlignment(Pos.CENTER);
		buttonsBox.setMinSize(500, 600);
		buttonsBox.setMaxSize(500, 600);
		logBox = new VBox(messageBox);
		logBox.setStyle("-fx-background-color: rgba(0,0,0 , 0.5);");
		borderPane.setRight(logBox);
		borderPane.setLeft(buttonsBox);
		borderPane.setAlignment(buttonsBox, Pos.CENTER);
		borderPane.setStyle("-fx-background-image: url(mocha.jpg);");

		setStartButtons();

		messageBox.setText("Welcome" + System.lineSeparator() + "Press \"Start Order\" to make a coffee" + System.lineSeparator() + "A coffee starts at $3.99");

		primaryStage.setScene(scene);
		primaryStage.show();

	}

	public void startPressed()
	{
		order = new BasicCoffee();
		resetCount();
		setOrderButtons();
		updateOrder();
	}

	public void deletePressed()
	{
		setStartButtons();
		messageBox.setText("Sorry for the trouble. Please come again soon.");
	}

	public void finishPressed()
	{
		setStartButtons();
		messageBox.setText("Thank you! Your total is:" + System.lineSeparator() + "$" + Math.round(order.makeCoffee()*100.0)/100.0);
	}

	public void creamPressed()
	{
		order = new Cream(order);
		creamCount++;
		updateOrder();
	}

	public void extraShotPressed()
	{
		order = new ExtraShot(order);
		extraShotCount++;
		updateOrder();
	}

	public void sugarPressed()
	{
		order = new Sugar(order);
		sugarCount++;
		updateOrder();
	}

	public void vanillaPressed()
	{
		order = new Vanilla(order);
		vanillaCount++;
		updateOrder();
	}

	public void whippedCreamPressed()
	{
		order = new WhippedCream(order);
		whippedCreamCount++;
		updateOrder();
	}

	//action when pressing Start Order
	public void setOrderButtons()
	{
		startButton.setDisable(true);
		deleteButton.setDisable(false);
		finishButton.setDisable(false);
		extraShotButton.setDisable(false);
		vanillaButton.setDisable(false);
		creamButton.setDisable(false);
		sugarButton.setDisable(false);
		whippedCreamButton.setDisable(false);
	}

	//action when pressing Delete or Finish Order
	public void setStartButtons()
	{
		startButton.setDisable(false);
		deleteButton.setDisable(true);
		finishButton.setDisable(true);
		extraShotButton.setDisable(true);
		vanillaButton.setDisable(true);
		creamButton.setDisable(true);
		sugarButton.setDisable(true);
		whippedCreamButton.setDisable(true);
	}

	//set all counts to 0
	public void resetCount()
	{
		creamCount = 0;
		extraShotCount = 0;
		sugarCount = 0;
		vanillaCount = 0;
		whippedCreamCount = 0;
	}

	//print out the up to date version of the order
	public void updateOrder()
	{
		 String message =
				"Current Order:" + System.lineSeparator() +
				extraShotCount + "x Extra Shot(s)" + System.lineSeparator() +
				vanillaCount + "x pump(s) of Vanilla" + System.lineSeparator() +
				creamCount + "x pour(s) of Cream" + System.lineSeparator() +
				sugarCount + "x packet(s) of Sugar"	+ System.lineSeparator() +
				whippedCreamCount + "x spray(s) of Whipped Cream" + System.lineSeparator() +
				"Total: $" + Math.round(order.makeCoffee()*100.0)/100.0;

		 messageBox.setText(message);
	}

}
